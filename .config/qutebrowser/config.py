config.load_autoconfig(False)
# =================================================================#
# =========================     Font    ===========================#
# =================================================================#
c.fonts.default_family = "JetBrainsMono Nerd Font"
c.fonts.default_size = "11pt"
c.fonts.completion.entry = '11pt "JetBrainsMono Nerd Font"'
c.fonts.debug_console = '11pt "JetBrainsMono Nerd Font"'
c.fonts.prompts = "default_size JetBrainsMono Nerd Font"
c.fonts.statusbar = '11pt "JetBrainsMono Nerd Font"'

# =================================================================#
# ============================   TAB   ============================#
# =================================================================#
c.tabs.favicons.show = "always"
c.tabs.favicons.scale = 1
c.tabs.background = True
c.tabs.last_close = "close"
c.tabs.position = "top"
c.tabs.show = "multiple"
c.tabs.padding = {"left": 2, "right": 2, "bottom": 2, "top": 2}
c.tabs.max_width = 250

# =================================================================#
# =========================  Statusbar ============================#
# =================================================================#
c.statusbar.show = "in-mode"
c.statusbar.position = "bottom"
c.tabs.select_on_remove = "prev"
c.statusbar.widgets = ["progress", "keypress", "url", "scroll", "history", "tabs"]

# =================================================================#
# ===========================  URL ================================#
# =================================================================#
# c.url.default_page = '~/prjcts/siteWeb/newtab/index.html'
# c.url.start_pages = '~/prjcts/siteWeb/newtab/index.html'
# c.url.default_page = 'https://start.duckduckgo.com/'
# c.url.start_pages = 'https://start.duckduckgo.com/'

# =================================================================#
# ===========================  Downloads ==========================#
# =================================================================#
c.downloads.location.directory = "~/Downloads/"
c.downloads.location.suggestion = "both"
c.downloads.location.remember = False
c.downloads.position = "bottom"
c.downloads.remove_finished = 5000

# =================================================================#
# ===========================  Content   ==========================#
# =================================================================#
c.content.autoplay = False
c.content.blocking.enabled = True
c.content.blocking.method = "auto"
c.content.cookies.accept = "all"
c.content.desktop_capture = "ask"
c.content.geolocation = False
c.content.headers.do_not_track = True
c.content.images = True
c.content.javascript.clipboard = "access"
c.content.javascript.enabled = True
c.content.media.audio_capture = "ask"
c.content.media.audio_video_capture = "ask"
c.content.media.video_capture = "ask"
c.content.notifications.enabled = "ask"
c.content.notifications.presenter = "auto"
c.content.pdfjs = False
c.content.private_browsing = False

# =================================================================#
# ===========================  Others =============================#
# =================================================================#
c.scrolling.bar = "never"
c.hints.leave_on_load = False
c.auto_save.session = True
c.scrolling.smooth = True
c.qt.highdpi = True
c.completion.height = 200
c.confirm_quit = ["multiple-tabs", "downloads"]
c.content.cookies.accept = "all"
c.colors.webpage.preferred_color_scheme = "dark"
c.editor.command = ["foot", "-e", "nvim", "{file}", "-c", "normal {line}G{column0}l"]
c.fileselect.multiple_files.command = ["foot", "-e", "ranger", "--choosefiles={}"]
# c.colors.webpage.darkmode.enabled = True
c.url.default_page = "https://start.duckduckgo.com"

c.url.searchengines = {
    "DEFAULT": "https://duckduckgo.com?q={}",
    "gg": "https://www.google.com/search?q={}",
    "yt": "https://www.youtube.com/results?search_query={}",
    "re": "https://www.reddit.com/search?q={}",
    "aw": "https://wiki.archlinux.org/?search={}",
    "dl": "https://deepl.com/translator#_/en/{}",
    "tr": "https://libretranslate.com/?q={}",
    "dd": "https://duckduckgo.com?q={}",
    "gh": "https://github.com/search?q={}",
    "gm": "https://mail.google.com/mail/u/0/#search/{}",
    "gp": "https://photos.google.com/search/{}",
}
c.aliases = {
    "adblock-toggle": "config-cycle -t content.blocking.enabled",
    "chromium": "spawn --detach chromium {url}",
    "firefox": "spawn --detach firefox {url}",
    "prv": "open --private",
    "mpv": "spawn --detach mpv {url}",
    "o": "open",
    "ot": "open -t",
    "q": "quit",
    "qa": "quit",
    "qa!": "quit",
    "q!": "quit",
}
# make "click to copy link" work
can_access_clipboard = (
    "https://*.atlassian.net/*",
    "https://github.com/*",
)
for url_pattern in can_access_clipboard:
    config.set("content.javascript.clipboard", "access", url_pattern)
# =================================================================#
# ===========================  Binds  =============================#
# =================================================================#
config.bind("xs", "config-cycle statusbar.show always never")
config.bind("xt", "config-cycle tabs.show always never")
config.bind(
    "xx",
    "config-cycle tabs.show always never;; config-cycle statusbar.show always never",
)
config.bind("<Ctrl-p>", "hint links spawn mpv {hint-url}")
config.bind("<Ctrl-o>", "prompt-open-download", mode="prompt")
config.bind("<Ctrl-e>", "cmd-edit", mode="command")
config.bind("<Ctrl-j>", "completion-item-focus next", mode="command")
config.bind("<Ctrl-k>", "completion-item-focus prev", mode="command")
# =================================================================#
# ====================== Gruvbox dark =============================#
# =================================================================#
# base16-qutebrowser (https://github.com/theova/base16-qutebrowser)
# Scheme name: Gruvbox Material Dark, Hard
# Scheme author: Mayush Kumar (https://github.com/MayushKumar), sainnhe (https://github.com/sainnhe/gruvbox-material-vscode)
# Template author: theova

