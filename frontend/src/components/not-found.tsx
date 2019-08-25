import React from 'react';
import { RouteComponentProps, withRouter } from 'react-router';

import { Button, ButtonGroup, Code, NonIdealState } from '@blueprintjs/core';
import { IconNames } from '@blueprintjs/icons';

export interface INotFoundProps {
  // empty
}

export const NotFound = withRouter(({ history, location }: INotFoundProps & RouteComponentProps) => {
  const description = (
    <span>
      <Code>{location.pathname}</Code> could not be found on the server.
    </span>
  );

  const goBack = React.useCallback(() => history.goBack(), [history]);

  return (
    <NonIdealState icon={IconNames.ISSUE} title="404 not found" description={description}>
      <ButtonGroup large minimal>
        <Button text="Go back" icon={IconNames.ARROW_LEFT} onClick={goBack} />
      </ButtonGroup>
    </NonIdealState>
  );
});
