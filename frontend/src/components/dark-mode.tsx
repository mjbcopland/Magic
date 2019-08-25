import React from 'react';

import { Classes, Hotkey, Hotkeys, HotkeysTarget } from '@blueprintjs/core';

export interface IDarkModeContext {
  enabled: boolean;
  enable: () => void;
  disable: () => void;
  toggle: () => void;
}

const _NOP = () => {
  // do nothing
};

const Context = React.createContext<IDarkModeContext>({ enabled: false, enable: _NOP, disable: _NOP, toggle: _NOP });

export const Provider = HotkeysTarget(
  class extends React.Component<{}, { enabled: boolean }> {
    public state = { enabled: false };

    public enable = () => {
      this.setState({ enabled: true }, () => document.body.classList.add(Classes.DARK));
    };

    public disable = () => {
      this.setState({ enabled: false }, () => document.body.classList.remove(Classes.DARK));
    };

    public toggle = () => {
      const { enabled } = this.state;
      return enabled ? this.disable() : this.enable();
    };

    public renderHotkeys() {
      return (
        <Hotkeys>
          <Hotkey global combo="shift + d" label="Toggle dark mode" onKeyDown={this.toggle} />
        </Hotkeys>
      );
    }

    public render() {
      const { enable, disable, toggle } = this;
      const { enabled } = this.state;

      const context = { enabled, enable, disable, toggle };

      return <Context.Provider value={context}>{this.props.children}</Context.Provider>;
    }
  }
);

export const DarkMode = { Consumer: Context.Consumer, Provider };
