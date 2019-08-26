import React from 'react';
import { Route, Switch } from 'react-router';
import { BrowserRouter } from 'react-router-dom';

import { hot } from 'react-hot-loader/root';

import { ApolloProvider } from '@apollo/react-common';

import { DarkMode } from '~/components/dark-mode';
import { ErrorBoundary } from '~/components/error-boundary';
import { Navigation } from '~/components/navigation';
import { NotFound } from '~/components/not-found';

import { Main } from '~/routes/main';
import { Worlds } from '~/routes/worlds';

import { client } from '~/apollo/client';

export const App = hot(() => (
  <DarkMode.HotkeysListener>
    <ApolloProvider client={client}>
      <BrowserRouter>
        <ErrorBoundary>
          <Navigation />
          <Switch>
            <Route exact strict path="/" component={Main} />
            <Route strict path="/worlds" component={Worlds} />
            <Route component={NotFound} />
          </Switch>
        </ErrorBoundary>
      </BrowserRouter>
    </ApolloProvider>
  </DarkMode.HotkeysListener>
));
