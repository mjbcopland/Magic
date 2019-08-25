import React from 'react';

import { ErrorView } from '~/components/error-view';

export interface IErrorBoundaryProps {
  children: React.ReactNode;
}

export interface IErrorBoundaryState {
  error: Maybe<Error>;
  info?: React.ErrorInfo;
}

export class ErrorBoundary extends React.Component<IErrorBoundaryProps, IErrorBoundaryState> {
  public state = { error: null, info: undefined };

  public componentDidCatch(error: Error, info?: React.ErrorInfo) {
    this.setState({ error, info });
  }

  public render() {
    const { children } = this.props;
    const { error } = this.state;
    return error ? <ErrorView error={error} /> : children;
  }
}

export const withErrorBoundary = <Props extends any>(Component: React.ComponentType<Props>) => {
  return (props: Props) => (
    <ErrorBoundary>
      <Component {...props} />
    </ErrorBoundary>
  );
};
