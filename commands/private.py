import cfg
import discord
import utils
import functions as func
from commands.base import Cmd
from time import time

help_text = [
    [
<<<<<<< HEAD
        ("Sposób Użycia:", "<PREFIX><COMMAND>"),
        ("Opis:",
         "Sprawa że Twój kanał głosowy jest prywatny i nikt w praost nie może do Ciebie Dołączyć.\n\n"
         "Tworzy kanał \"⇩ Dołącz (username)\" nad lub pod tobą aby ludzie mogli dołaczyć. "
         "Kiedy ktoś wejdzie na kanał prześolę Ci powadomienie z prośbą o dołączenie."
         "Możesz ją zaakceptować, zignorować lub zablokować, blokada ukrywa kanał dla użytkownika."),
=======
        ("Usage:", "<PREFIX><COMMAND>"),
        (
            "Description:",
            "Make your voice channel private, preventing anyone from joining you directly.\n\n"
            'Creates a "⇩ Join (username)" channel above yours so people can request to join you. '
            "When someone joins that channel, I'll send you a message asking you to "
            "approve/deny/block their request.",
        ),
>>>>>>> 17698450c6f885ae3ee3dae059754ba72931adf6
    ]
]


async def execute(ctx, params):
    guild = ctx["guild"]
    settings = ctx["settings"]
    author = ctx["message"].author
    vc = ctx["voice_channel"]

    for p, pv in settings["auto_channels"].items():
        for s, sv in pv["secondaries"].items():
            if s == vc.id:
<<<<<<< HEAD
                if 'priv' in sv and sv['priv']:
                    return False, ("Twój kanał jest już prywatny. "
                                   "Użyj `{}public` Aby by znowu publiczny.".format(ctx['print_prefix']))
=======
                if "priv" in sv and sv["priv"]:
                    return False, (
                        "Your channel is already private. "
                        "Use `{}public` to make it public again.".format(ctx["print_prefix"])
                    )
>>>>>>> 17698450c6f885ae3ee3dae059754ba72931adf6
                try:
                    await vc.set_permissions(author, connect=True)
                    await vc.set_permissions(guild.default_role, connect=False)
                except discord.errors.Forbidden:
<<<<<<< HEAD
                    return False, ("Nie mam do tego permisji."
                                   "Upewnij się że mam pozwolenie *permisje* do *Zarządzanie Rolami* w tej kategorii i serwerze.")
                settings['auto_channels'][p]['secondaries'][s]['priv'] = True
                settings['auto_channels'][p]['secondaries'][s]['msgs'] = ctx['channel'].id
=======
                    return False, (
                        "I don't have permission to do that."
                        "Please make sure I have the *Manage Roles* permission in this server and category."
                    )
                settings["auto_channels"][p]["secondaries"][s]["priv"] = True
                settings["auto_channels"][p]["secondaries"][s]["msgs"] = ctx["channel"].id
>>>>>>> 17698450c6f885ae3ee3dae059754ba72931adf6
                utils.set_serv_settings(guild, settings)
                cfg.PRIV_CHANNELS[s] = {
                    "creator": author,
                    "voice_channel": vc,
                    "primary_id": p,
                    "text_channel": ctx["channel"],
                    "guild_id": guild.id,
                    "request_time": time(),
                    "prefix": ctx["print_prefix"],
                }
<<<<<<< HEAD
                return True, ("Twój kanał jest teraz *PRYWATNY!*\n"
                              "Tworzy kanał \"⇩ Dołącz (username)\" nad lub pod tobą aby ludzie mogli dołaczyć. "
                              "Kiedy ktoś wejdzie na kanał prześolę Ci powadomienie z prośbą o dołączenie."
                              "Możesz ją zaakceptować, zignorować lub zablokować, blokada ukrywa kanał dla użytkownika.\n"
                              "Użyj `{}public` Aby kanał był znowu otwarty."
                              "".format(func.esc_md(author.display_name), ctx['print_prefix']))
    return False, "Wygląda na to że nie jesteś już na kanale głosowym."
=======
                return True, (
                    "Your channel is now private!\n"
                    'A "**⇩ Join {}**" channel will appear above your one shortly. '
                    "When someone enters this channel to request to join you, "
                    "I'll send a message here asking you to approve or deny their request.\n"
                    "Use `{}public` to make it public again."
                    "".format(func.esc_md(author.display_name), ctx["print_prefix"])
                )
    return False, "It doesn't seem like you're in a voice channel anymore."
>>>>>>> 17698450c6f885ae3ee3dae059754ba72931adf6


command = Cmd(
    execute=execute,
    help_text=help_text,
    params_required=0,
    admin_required=False,
    voice_required=True,
    creator_only=True,
)
