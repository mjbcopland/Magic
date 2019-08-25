import React from 'react';
import { Route, Switch } from 'react-router';
import { BrowserRouter } from 'react-router-dom';

import { hot } from 'react-hot-loader/root';

import { DarkMode } from '~/components/dark-mode';
import { ErrorBoundary } from '~/components/error-boundary';
import { Navigation } from '~/components/navigation';
import { NotFound } from '~/components/not-found';

import { Main } from '~/routes/main';

export const App = hot(() => (
  <DarkMode.Provider>
    <BrowserRouter>
      <ErrorBoundary>
        <Navigation />
        <Switch>
          <Route exact strict path="/" component={Main} />
          <Route component={NotFound} />
        </Switch>
      </ErrorBoundary>
    </BrowserRouter>
  </DarkMode.Provider>
));
