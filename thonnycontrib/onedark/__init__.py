from thonny import get_workbench
from thonny.workbench import SyntaxThemeSettings


def one_dark() -> SyntaxThemeSettings:
    '''
    One Dark Color Scheme

    Ideas taken from:
    https://github.com/joshdick/onedark.vim/
    '''
    BLACK = '#282c34'
    WHITE = '#abb2bf'
    GREEN = '#98c379'
    RED = '#e06c75'
    YELLOW = '#e5c07b'
    BLUE = '#61afef'
    MAGENTA = '#c678dd'
    CYAN = '#56b6c2'
    GRAY_GUTTER = '#4b5263'
    GRAY_COMMENT = '#5c6370'
    GRAY_CURSOR = '#2c323c'
    GRAY_SELECTION_FG = None
    GRAY_SELECTION_BG = '#3E4452'

    return {
        # Editor
        'tab': {
            'background': WHITE,
        },
        'TEXT': {
            'foreground': WHITE,
            'insertbackground': WHITE,
            'background': BLACK,
        },
        'GUTTER': {
            'foreground': GRAY_GUTTER,
            'background': BLACK,
        },
        'keyword': {
            'foreground': MAGENTA,
        },
        'builtin': {
            'foreground': YELLOW,
        },
        'definition': {
            'foreground': BLUE,
        },
        'current_line': {
            'background': GRAY_CURSOR,
        },
        'sel': {
            'foreground': GRAY_SELECTION_FG,
            'background': GRAY_SELECTION_BG,
        },
        'comment': {
            'foreground': GRAY_COMMENT,
        },
        'number': {
            'foreground': RED,
        },
        'string': {
            'foreground': GREEN,
        },
        'string3': {
            'foreground': GREEN,
        },
        'open_string': {
            'foreground': WHITE,
            'background': RED,
        },
        'open_string3': {
            'foreground': WHITE,
            'background': RED,
        },
        'surrounding_parens': {
            'foreground': WHITE,
        },
        'unclosed_expression': {
            'background': RED,
        },

        # Shell
        'prompt': {
            'foreground': CYAN,
        },
        'stdin': {
            'foreground': CYAN,
        },
        'stdout': {
            'foreground': WHITE,
        },
        'stderr': {
            'foreground': RED,
        },
        'value': {
            'foreground': YELLOW,
        },

        # Debugger
        'active_focus': {
            'background': GRAY_SELECTION_BG,
        },
    }


def load_plugin() -> None:
    get_workbench().add_syntax_theme('One Dark', 'Default Dark', one_dark)