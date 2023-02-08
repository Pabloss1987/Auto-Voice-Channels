import cfg
import discord
import utils
from commands.base import Cmd

help_text = [
    [
<<<<<<< HEAD
        ("Sposób Użycia:", "<PREFIX><COMMAND>"),
        ("Opis:",
         "Zmienia Twój Kanał na publiczny, po tym każdy będzie mógł do Ciebie dołączyć."),
=======
        ("Usage:", "<PREFIX><COMMAND>"),
        ("Description:", "Make your private channel public again, so anyone can join."),
>>>>>>> 17698450c6f885ae3ee3dae059754ba72931adf6
    ]
]


async def execute(ctx, params):
    guild = ctx["guild"]
    settings = ctx["settings"]
    vc = ctx["voice_channel"]

    for p, pv in settings["auto_channels"].items():
        for s, sv in pv["secondaries"].items():
            if s == vc.id:
<<<<<<< HEAD
                if 'priv' not in sv or not sv['priv']:
                    return False, ("Twój kanał jest już publiczny. "
                                   "Użyj `{}private` aby był znowu prywatny.".format(ctx['print_prefix']))
                try:
                    await vc.set_permissions(guild.default_role, connect=True)
                except discord.errors.Forbidden:
                    return False, ("Nie mam do tego Permisji."
                                   "Upewnij się że mam pozwolenie *permisje* do *Zarządzanie Rolami* w tej kategorii i serwerze.")
                settings['auto_channels'][p]['secondaries'][s]['priv'] = False
=======
                if "priv" not in sv or not sv["priv"]:
                    return False, (
                        "Your channel is already public. "
                        "Use `{}private` to make it private instead.".format(ctx["print_prefix"])
                    )
                try:
                    await vc.set_permissions(guild.default_role, connect=True)
                except discord.errors.Forbidden:
                    return False, (
                        "I don't have permission to do that."
                        "Please make sure I have the *Manage Roles* permission in this server and category."
                    )
                settings["auto_channels"][p]["secondaries"][s]["priv"] = False
>>>>>>> 17698450c6f885ae3ee3dae059754ba72931adf6
                try:
                    jcid = settings["auto_channels"][p]["secondaries"][s]["jc"]
                    del settings["auto_channels"][p]["secondaries"][s]["jc"]
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
