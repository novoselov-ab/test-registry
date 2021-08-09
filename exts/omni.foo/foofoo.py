import omni.kit.app
import omni.ext

class Foofoo(omni.ext.IExt):
    def on_startup(self):
        app = omni.kit.app.get_app()
        self._update_sub = app.get_update_event_stream().create_subscription_to_pop(
            self._on_update
        )
        self._cnt = 0

    def on_shutdown(self):
        self._update_sub = None

    def _on_update(self, _):
        if self._cnt % 1000 == 0:
            print('cnt', self._cnt)
        self._cnt += 1


