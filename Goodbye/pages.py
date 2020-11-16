from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


### Testing ###


### App-Pages ###

class RewardPage(Page):
    form_model = "player"
    form_fields = ["reward"]

    # display only if consent is accpeted
    def is_displayed(self):
        return self.participant.vars["timeout"] == 0




class GoodbyePageVPN(Page):
    form_model = "player"
    form_fields = []

    # display page conditionally
    def is_displayed(self):
        return self.player.reward == 1




class GoodbyePageMoney(Page):
    form_model = "player"
    form_fields = []

    # timeout
    #timeout_seconds = 1200

    def is_displayed(self):
        return self.player.reward == 2



class VorletztePage(Page):
    form_model = "player"
    form_fields = ["anmerkungen"]



class LastPage(Page):
    form_model = "player"

class Debriefing(Page):
    form_model = "player"



### Page sequence ###
page_sequence = [#RewardPage,
                 #GoodbyePageVPN,
                 #GoodbyePageMoney,
                 VorletztePage,
                 Debriefing,
                 LastPage]
