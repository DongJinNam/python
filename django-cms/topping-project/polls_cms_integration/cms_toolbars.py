from cms.utils.urlutils import admin_reverse
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from polls.models import Poll


class PollToolbar(CMSToolbar):

    def populate(self):
        buttonlist = self.toolbar.add_button_list()

        buttonlist.add_sideframe_button(
            name='Poll list',
            url=admin_reverse('polls_poll_changelist'),
        )

        buttonlist.add_modal_button(
            name = 'Add a new poll',
            url = admin_reverse('polls_poll_add'),
        )


toolbar_pool.register(PollToolbar)