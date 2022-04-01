import cfg
import discord
import utils
from commands.base import Cmd

help_text = [
    [
        ("Sposób Użycia:", "<PREFIX><COMMAND>"),
        ("Opis:",
         "Zmienia Twój Kanał na publiczny i każdy może do niego dołączyć."),
    ]
]


async def execute(ctx, params):
    guild = ctx['guild']
    settings = ctx['settings']
    vc = ctx['voice_channel']

    for p, pv in settings['auto_channels'].items():
        for s, sv in pv['secondaries'].items():
            if s == vc.id:
                if 'priv' not in sv or not sv['priv']:
                    return False, ("Twój kanał jest już publiczny. "
                                   "Użyj `{}private` aby był znowu prywatny.".format(ctx['print_prefix']))
                try:
                    await vc.set_permissions(guild.default_role, connect=True)
                except discord.errors.Forbidden:
                    return False, ("Nie mam do tego Permisji."
                                   "Upewnij się że mam pozwolenie "permisje" do *Zarządzanie Rolami* w tej kategorii i serwerze.")
                settings['auto_channels'][p]['secondaries'][s]['priv'] = False
                try:
                    jcid = settings['auto_channels'][p]['secondaries'][s]['jc']
                    del settings['auto_channels'][p]['secondaries'][s]['jc']
                except KeyError:
                    jcid = 0
                utils.set_serv_settings(guild, settings)
                if s in cfg.PRIV_CHANNELS:
                    del cfg.PRIV_CHANNELS[s]
                try:
                    jc = guild.get_channel(jcid)
                    if jc:
                        await jc.delete()
                except discord.errors.Forbidden:
                    return False, "Tój kanał jest teraz publiczny ale nie mogę skasować kanału **⇩ Dołącz** ."
                return True, "Twój kanał jest *PUBLICZNY!*"
    return False, "Wygląda na to że nie jesteś już na kanale głosowym."


command = Cmd(
    execute=execute,
    help_text=help_text,
    params_required=0,
    admin_required=False,
    voice_required=True,
    creator_only=True,
)
