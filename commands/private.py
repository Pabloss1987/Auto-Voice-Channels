import cfg
import discord
import utils
import functions as func
from commands.base import Cmd
from time import time

help_text = [
    [
        ("Sposób Użycia:", "<PREFIX><COMMAND>"),
        ("Opis:",
         "Sprawa że Twój kanał głosowy jest prywatny i nikt w praost nie może do Ciebie Dołączyć.\n\n"
         "Tworzy kanał \"⇩ Dołącz (username)\" nad lub pod tobą aby ludzie mogli dołaczyć. "
         "Kiedy ktoś wejdzie na kanał prześolę Ci powadomienie z prośbą o dołączenie."
         "Możesz ją zaakceptować, zignorować lub zablokować, blokada ukrywa kanał dla użytkownika."),
    ]
]


async def execute(ctx, params):
    guild = ctx['guild']
    settings = ctx['settings']
    author = ctx['message'].author
    vc = ctx['voice_channel']

    for p, pv in settings['auto_channels'].items():
        for s, sv in pv['secondaries'].items():
            if s == vc.id:
                if 'priv' in sv and sv['priv']:
                    return False, ("Twój kanał jest już prywatny. "
                                   "Użyj `{}public` Aby by znowu publiczny.".format(ctx['print_prefix']))
                try:
                    await vc.set_permissions(author, connect=True)
                    await vc.set_permissions(guild.default_role, connect=False)
                except discord.errors.Forbidden:
                    return False, ("Nie mam do tego permisji."
                                   "Upewnij się że mam pozwolenie "permisje" do *Zarządzanie Rolami* w tej kategorii i serwerze.")
                settings['auto_channels'][p]['secondaries'][s]['priv'] = True
                settings['auto_channels'][p]['secondaries'][s]['msgs'] = ctx['channel'].id
                utils.set_serv_settings(guild, settings)
                cfg.PRIV_CHANNELS[s] = {
                    'creator': author,
                    'voice_channel': vc,
                    'primary_id': p,
                    'text_channel': ctx['channel'],
                    'guild_id': guild.id,
                    'request_time': time(),
                    'prefix': ctx['print_prefix'],
                }
                return True, ("Twój kanał jest teraz *PRYWATNY!*\n"
                              "Tworzy kanał \"⇩ Dołącz (username)\" nad lub pod tobą aby ludzie mogli dołaczyć. "
                              "Kiedy ktoś wejdzie na kanał prześolę Ci powadomienie z prośbą o dołączenie."
                              "Możesz ją zaakceptować, zignorować lub zablokować, blokada ukrywa kanał dla użytkownika.\n"
                              "Użyj `{}public` Aby kanał był znowu otwarty."
                              "".format(func.esc_md(author.display_name), ctx['print_prefix']))
    return False, "Wygląda na to że nie jesteś już na kanale głosowym."


command = Cmd(
    execute=execute,
    help_text=help_text,
    params_required=0,
    admin_required=False,
    voice_required=True,
    creator_only=True,
)
