import { InMemoryCache } from 'apollo-cache-inmemory';
import { ApolloClient } from 'apollo-client';
import { ApolloLink } from 'apollo-link';
import { ErrorHandler, onError } from 'apollo-link-error';
import { createHttpLink } from 'apollo-link-http';

const errorHandler: ErrorHandler = ({ graphQLErrors = [], networkError }) => {
  if (networkError) console.error(networkError);
  graphQLErrors.forEach((graphQLError) => console.error(graphQLError));
};

export const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: ApolloLink.from([onError(errorHandler), createHttpLink({ uri: '/api/graphql', credentials: 'same-origin' })]),
});
