from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse
from .forms import ConsumerForm, ConsumerExchangeForm, AccessTokenDataForm

from oauth2_provider.compat import urlencode


class ConsumerView(FormView):
    form_class = ConsumerForm
    success_url = '/consumer/'
    template_name = 'consumer/consumer.html'

    def __init__(self, **kwargs):
        self.authorization_link = None
        super(ConsumerView, self).__init__(**kwargs)

    def get_success_url(self):
        url = super(ConsumerView, self).get_success_url()
        return '{url}?{qs}'.format(
            url=url,
            qs=urlencode({'authorization_link': self.authorization_link})
        )

    def get(self, request, *args, **kwargs):
        kwargs['authorization_link'] = request.GET.get(
            'authorization_link',
            None
        )

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
            self.get_context_data(form=form, **kwargs)
        )

    def post(self, request, *args, **kwargs):
        self.request = request
        return super(ConsumerView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        qs = urlencode({
            'client_id': form.cleaned_data['client_id'],
            'response_type': 'code',
            'state': 'random_state_string',
        })
        self.authorization_link = "{url}?{qs}".format(
            url=form.cleaned_data['authorization_url'],
            qs=qs
        )
        return super(ConsumerView, self).form_valid(form)


class ConsumerExchangeView(FormView):
    form_class = ConsumerExchangeForm
    template_name = 'consumer/consumer-exchange.html'

    def get(self, request, *args, **kwargs):
        try:
            self.initial = {
                'code': request.GET['code'],
                'state': request.GET['state'],
                'redirect_url': request.build_absolute_uri(
                    reverse('consumer-exchange')
                )
            }
        except KeyError:
            kwargs['noparams'] = True

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
            self.get_context_data(form=form, **kwargs)
        )


class ConsumerDoneView(TemplateView):
    template_name = 'consumer/consumer-done.html'

    def get(self, request, *args, **kwargs):
        if 'access_token' in request.GET:
            form = AccessTokenDataForm(initial={
                'access_token': request.GET.get('access_token', None),
                'token_type': request.GET.get('token_type', None),
                'expires_in': request.GET.get('expires_in', None),
                'refresh_token': request.GET.get('refresh_token', None),
            })
            kwargs['form'] = form

        return super(ConsumerDoneView, self).get(request, *args, **kwargs)
