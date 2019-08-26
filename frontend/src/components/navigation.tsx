import React from 'react';
import { RouteComponentProps, withRouter } from 'react-router';

import { Alignment, Button, ButtonGroup, Icon, Navbar } from '@blueprintjs/core';
import { IconNames } from '@blueprintjs/icons';

import { DarkModeSwitch } from '~/components/dark-mode-switch';

export const Navigation = withRouter(({ history }: RouteComponentProps) => (
  <Navbar>
    <Navbar.Group>
      <Navbar.Heading>Magic</Navbar.Heading>
      <Navbar.Divider />
      <ButtonGroup minimal>
        <Button text="Home" onClick={() => history.push('/')} />
        <Button text="Worlds" onClick={() => history.push('/worlds')} />
      </ButtonGroup>
    </Navbar.Group>
    <Navbar.Group align={Alignment.RIGHT}>
      <DarkModeSwitch alignIndicator={Alignment.RIGHT} style={{ margin: 0 }}>
        <Icon icon={IconNames.MOON} />
      </DarkModeSwitch>
    </Navbar.Group>
  </Navbar>
));
