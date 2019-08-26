import React from 'react';

import { Alignment, Icon, Navbar } from '@blueprintjs/core';
import { IconNames } from '@blueprintjs/icons';

import { DarkModeSwitch } from '~/components/dark-mode-switch';

export const Navigation = () => (
  <Navbar>
    <Navbar.Group>
      <Navbar.Heading>Magic</Navbar.Heading>
    </Navbar.Group>
    <Navbar.Group align={Alignment.RIGHT}>
      <DarkModeSwitch alignIndicator={Alignment.RIGHT} style={{ margin: 0 }}>
        <Icon icon={IconNames.MOON} />
      </DarkModeSwitch>
    </Navbar.Group>
  </Navbar>
);
