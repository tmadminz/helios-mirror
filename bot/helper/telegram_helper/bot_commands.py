import os
def getCommand(name: str, command: str):
    try:
        if len(os.environ[name]) == 0:
            raise KeyError
        return os.environ[name]
    except KeyError:
        return command

class _BotCommands:
    def __init__(self):
        self.StartCommand = getCommand('START_COMMAND', 'start')
        self.MirrorCommand = getCommand('MIRROR_COMMAND', 'mirror2')
        self.UnzipMirrorCommand = getCommand('UNZIP_COMMAND', 'unzipmirror2')
        self.ZipMirrorCommand = getCommand('ZIP_COMMAND', 'zipmirror2')
        self.CancelMirror = getCommand('CANCEL_COMMAND', 'cancel2')
        self.CancelAllCommand = getCommand('CANCEL_ALL_COMMAND', 'cancelall')
        self.ListCommand = getCommand('LIST_COMMAND', 'list')
        self.SearchCommand = getCommand('SEARCH_COMMAND', 'search2')
        self.StatusCommand = getCommand('STATUS_COMMAND', 'status2')
        self.AuthorizedUsersCommand =  getCommand('USERS_COMMAND', 'users2')
        self.AuthorizeCommand =  getCommand('AUTH_COMMAND', 'authorize2')
        self.UnAuthorizeCommand = getCommand('UNAUTH_COMMAND','unauthorize2')
        self.AddSudoCommand = getCommand('ADDSUDO_COMMAND', 'addsudo2')
        self.RmSudoCommand = getCommand('RMSUDO_COMMAND', 'rmsudo2')
        self.AddModCommand = getCommand('ADDMOD_COMMAND', 'addmod2')
        self.RmModCommand = getCommand('RMMOD_COMMAND', 'rmmod2')
        self.PingCommand =  getCommand('PING_COMMAND','ping')
        self.RestartCommand =  getCommand('RESTART_COMMAND', 'restart2')
        self.StatsCommand = getCommand('STATS_COMMAND', 'stats2')
        self.HelpCommand = getCommand('HELP_COMMAND', 'help')
        self.LogCommand = getCommand('LOG_COMMAND' , 'log2')
        self.SpeedCommand = getCommand('SPEEDTEST_COMMAND', 'speedtest2')
        self.CloneCommand = getCommand('CLONE_COMMAND', 'clone2')
        self.CountCommand = getCommand('COUNT_COMMAND', 'count2')
        self.WatchCommand = getCommand('WATCH_COMMAND', 'watch2')
        self.ZipWatchCommand = getCommand('ZIPWATCH_COMMAND', 'zipwatch2')
        self.QbMirrorCommand = getCommand('QBMIRROR_COMMAND', 'qbmirror2')
        self.QbUnzipMirrorCommand = getCommand('QBUNZIP_COMMAND', 'qbunzipmirror2')
        self.QbZipMirrorCommand = getCommand('QBZIP_COMMAND', 'qbzipmirror2')
        self.DeleteCommand = getCommand('DELETE_COMMAND', 'del2')
        self.ShellCommand = getCommand('SHELL_COMMAND', 'shell2')
        self.ExecHelpCommand = getCommand('EXEHELP_COMMAND', 'exechelp2')
        self.LeechSetCommand = getCommand('LEECHSET_COMMAND', 'leechset2')
        self.SetThumbCommand = getCommand('SETTHUMB_COMMAND', 'setthumb2')
        self.LeechCommand = getCommand('LEECH_COMMAND', 'leech2')
        self.UnzipLeechCommand = getCommand('UNZIPLEECH_COMMAND', 'unzipleech2')
        self.ZipLeechCommand = getCommand('ZIPLEECH_COMMAND', 'zipleech2')
        self.QbLeechCommand = getCommand('QBLEECH_COMMAND', 'qbleech2')
        self.QbUnzipLeechCommand = getCommand('QBUNZIPLEECH_COMMAND', 'qbunzipleech2')
        self.QbZipLeechCommand = getCommand('QBZIPLEECH_COMMAND', 'qbzipleech2')
        self.LeechWatchCommand = getCommand('LEECHWATCH_COMMAND', 'leechwatch2')
        self.LeechZipWatchCommand = getCommand('LEECHZIPWATCH_COMMAND', 'leechzipwatch2')
        self.TorrentSearchCommand = getCommand('TOR_COMMAND', 'ts2')
        self.RssListCommand = getCommand('RSSLIST_COMMAND', 'rsslist')
        self.RssGetCommand = getCommand('RSSGET_COMMAND', 'rssget')
        self.RssSubCommand = getCommand('RSSSUB_COMMAND', 'rsssub')
        self.RssUnSubCommand = getCommand('RSSUNSUB_COMMAND', 'rssunsub')
        self.RssUnSubAllCommand = getCommand('RSSUNSUBALL_COMMAND', 'rssunsuball')
        self.AddleechlogCommand = getCommand('ADDLEECHLOG_COMMAND', 'addll')
        self.RmleechlogCommand = getCommand('RMLEECHLOG_COMMAND', 'rmll')
        self.AddleechlogaltCommand = getCommand('ADDLEECHLOGALT_COMMAND', 'addleechlog')
        self.RmleechlogaltCommand = getCommand('RMLEECHLOGALT_COMMAND', 'rmleechlog')


BotCommands = _BotCommands()
