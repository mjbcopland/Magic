import React from 'react';
import { RouteComponentProps, withRouter } from 'react-router';

import { Button, ButtonGroup, Classes, NonIdealState, Position, Tooltip } from '@blueprintjs/core';
import { IconNames } from '@blueprintjs/icons';

export interface IErrorViewProps {
  error: Maybe<Error>;
}

export const ErrorView = withRouter(({ error, history }: IErrorViewProps & RouteComponentProps) => {
  const description = (
    <span>
      An{' '}
      <Tooltip content={error ? error.message : 'Unknown error'} position={Position.TOP}>
        <span className={Classes.TOOLTIP_INDICATOR}>unexpected error</span>
      </Tooltip>{' '}
      occurred when loading this page.
    </span>
  );

  const goBack = React.useCallback(() => history.goBack(), [history]);

  return error == null ? null : (
    <NonIdealState icon={IconNames.ERROR} title="Something went wrong" description={description}>
      <ButtonGroup large minimal>
        <Button text="Go back" icon={IconNames.ARROW_LEFT} onClick={goBack} />
        <Button text="Try again" icon={IconNames.REFRESH} />
      </ButtonGroup>
    </NonIdealState>
  );
});
