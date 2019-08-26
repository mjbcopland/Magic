import React from 'react';

import { useQuery } from '@apollo/react-hooks';
import { NonIdealState, Spinner } from '@blueprintjs/core';

import query from '~/graphql/hello-world.gql';

export const Main = () => {
  const { error, loading, data } = useQuery(query);

  if (error) throw error;

  const title = loading ? <Spinner size={Spinner.SIZE_SMALL} /> : data.helloWorld;

  return <NonIdealState title={title} />;
};
