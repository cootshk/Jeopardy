class colors:
    """
    A library for using colored text for print() statements
    """
  #colors
    okpink = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
  #Aliases
    red = fail
    blue = okblue
    white = endc
    orange = warning
    warn = warning
    uline = underline
    green = okgreen
    cyan = okcyan
    pink = okpink
    black = white #light mode imagine
    default = white
  #Letters
    w = white
    p = pink
    b = blue
    c = cyan
    g = green
    o = orange
    r = red
    u = uline
    f = fail
    d = default
    bk = black
    #clear screen
    def clear() -> None:
        """
        Clears the screen
        """
        import os
        os.system("cls" if os.name == "nt" else "clear")
class backgrounds:
    """
    Background colors for the print() statement
    """
  #Backgrounds
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'
  #Aliases
    bl = black
    r = red
    g = green
    o = orange
    b = blue
    p = purple
    c = cyan
    lg = lightgrey
if __name__ == "__main__":
  print(f"This is a {colors.g}library!{colors.w} Use {colors.b}from pcolors import colors as c, backgrounds as b{colors.w} to use the colors!")