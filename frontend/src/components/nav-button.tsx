import React from 'react';
import { Route, RouteProps } from 'react-router';

import { Button, IButtonProps } from '@blueprintjs/core';

export interface INavButtonProps extends IButtonProps, RouteProps {
  to: string;
}

export const NavButton = ({ to, ...props }: INavButtonProps) => (
  <Route {...props}>
    {({ match, history }) => {
      const handleClick = () => history.push(to);
      return <Button active={match != null} onClick={handleClick} {...props} />;
    }}
  </Route>
);
