<div align="center">

# oxocarbon-wezterm

</div>

<div align="center">

[![Stars](https://img.shields.io/github/stars/nyoom-engineering/oxocarbon?color=%23b66467&style=for-the-badge)](https://github.com/nyoom-engineering/oxocarbon/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/nyoom-engineering/oxocarbon?color=%238c977d&style=for-the-badge)](https://github.com/nyoom-engineering/oxocarbon/issues)
[![License](https://img.shields.io/github/license/nyoom-engineering/oxocarbon?color=%238da3b9&style=for-the-badge)](https://mit-license.org/)
![Discord Server](https://img.shields.io/discord/1050624267592663050?color=738adb&label=Discord&Color=white&style=for-the-badge)

</div>

Oxocarbon is a set of community ports of IBM's carbon color palette and design philosophy to various applications and tooling.

## Showcase

![neofetch](assets/neofetch.png)
![colorbars](assets/colorbars.png)

## Install

1. Run the following commands:

```bash
mkdir -p $HOME/.config/wezterm/colors
cd $HOME/.config/wezterm/colors/
curl -O https://raw.githubusercontent.com/nyoom-engineering/oxocarbon-wezterm/main/oxocarbon-dark.toml
```

2. Set it up as your colorscheme in your `wezterm.lua`

```lua
return {
  color_scheme = 'Oxocarbon Dark',
  use_fancy_tab_bar = false,
}
```

3. (optional) for a better experience consider enable this settings:

```lua
return {
  window_decorations = "RESIZE",
  hide_tab_bar_if_only_one_tab = true,
}
```

## License

The project is licensed under the MIT license
