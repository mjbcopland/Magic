import React from 'react';

import { ISwitchProps, Switch } from '@blueprintjs/core';

import { DarkMode } from '~/components/dark-mode';

export interface IDarkModeSwitchProps extends Omit<ISwitchProps, 'checked' | 'onChange'> {}

export const DarkModeSwitch = (props: IDarkModeSwitchProps) => {
  const context = React.useContext(DarkMode.Context);
  const checked = context.enabled;

  const disabled = (checked && context.disable == null) || (!checked && context.enable == null);

  const handleChange = React.useCallback(
    (event: React.FormEvent<HTMLInputElement>) => {
      if (event.currentTarget.checked) {
        if (context.enable) context.enable();
      } else {
        if (context.disable) context.disable();
      }
    },
    [context.enable, context.disable]
  );

  return <Switch checked={checked} disabled={disabled} onChange={handleChange} {...props} />;
};
