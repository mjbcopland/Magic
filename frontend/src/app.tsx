import React from 'react';
import { Route, Switch } from 'react-router';
import { BrowserRouter } from 'react-router-dom';

import { hot } from 'react-hot-loader/root';

import { Navbar } from '@blueprintjs/core';

import { DarkMode } from '~/components/dark-mode';
import { ErrorBoundary } from '~/components/error-boundary';
import { Main } from '~/routes/main';

import { name as title } from '../package.json';

export const App = hot(() => (
  <DarkMode.Provider>
    <BrowserRouter>
      <ErrorBoundary>
        <Navbar>
          <Navbar.Group>
            <Navbar.Heading>{title}</Navbar.Heading>
          </Navbar.Group>
        </Navbar>
        <Switch>
          <Route component={Main} />
        </Switch>
      </ErrorBoundary>
    </BrowserRouter>
  </DarkMode.Provider>
));
