import logging
from django.http import JsonResponse, Http404
from django.views import View


logger = logging.getLogger(__name__)


class BaseView(View):

    def dispatch(self, request, *args, **kwargs):
        try:
            response = super().dispatch(request, *args, **kwargs)
        except Http404 as e:
            raise e
        except Exception as e:
            logger.error('{} - {}'.format(e, request.path))
            return self._response({'errorMessage': str(e)}, status=400)

        if isinstance(response, (dict, list)):
            return self._response(response)
        else:
            return response

    @staticmethod
    def _response(data, status=200):
        return JsonResponse(data,
                            status=status)
