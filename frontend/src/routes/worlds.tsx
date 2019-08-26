import Fuse from 'fuse.js';
import React from 'react';

import { useMutation, useQuery } from '@apollo/react-hooks';
import { Alignment, Button, H3, Icon, Menu, NonIdealState, Spinner } from '@blueprintjs/core';
import { IconNames } from '@blueprintjs/icons';
import { ItemListPredicate, ItemRenderer, Select } from '@blueprintjs/select';

import { DocumentNode } from 'graphql';

declare module '~/graphql/worlds.gql' {
  export const CreateWorld: DocumentNode;
  export const GetWorlds: DocumentNode;
}

import { CreateWorld, GetWorlds } from '~/graphql/worlds.gql';

interface World {
  id: string;
  size: number;
  name: string;
}

type ICreateNewItemRendererArgs = [string, boolean, React.EventHandler<React.MouseEvent<HTMLElement>>];
type ICreateNewItemRenderer = (...args: ICreateNewItemRendererArgs) => JSX.Element | undefined;

const itemRenderer: ItemRenderer<Partial<World>> = (item, { index, handleClick, modifiers }) => {
  const { matchesPredicate, ...props } = modifiers;
  return matchesPredicate ? <Menu.Item key={index} text={item.name} onClick={handleClick} {...props} /> : null;
};

const createNewItemRenderer: ICreateNewItemRenderer = (query, active, handleClick) => {
  return <Menu.Item text={`Create '${query}'`} active={active} icon={IconNames.ADD} onClick={handleClick} />;
};

const createNewItemFromQuery = (query: string) => {
  return { name: query };
};

const itemListPredicate: ItemListPredicate<Partial<World>> = (query, items) => {
  return query ? new Fuse(items, { keys: ['name'] }).search(query) : items;
};

export const Worlds = () => {
  const [world, setWorld] = React.useState<World>();

  const { error, loading, data, refetch } = useQuery(GetWorlds);
  const [createWorld] = useMutation(CreateWorld);

  const handleItemSelect = React.useCallback(
    async (item) => {
      if (item.id == null) {
        const { name = '', size = 0 } = item;
        await createWorld({ variables: { world: { name, size } } });
        await refetch();
      }
      setWorld(item);
    },
    [refetch, createWorld, setWorld]
  );

  if (error) throw error;

  const { worlds = [] } = data || {};

  const rightIcon = loading ? (
    <Spinner size={Spinner.SIZE_SMALL} />
  ) : (
    <Icon icon={IconNames.CHEVRON_DOWN} iconSize={Icon.SIZE_LARGE} />
  );

  return (
    <Select<Partial<World>>
      items={worlds}
      itemRenderer={itemRenderer}
      itemListPredicate={itemListPredicate}
      createNewItemFromQuery={createNewItemFromQuery}
      createNewItemRenderer={createNewItemRenderer}
      onItemSelect={handleItemSelect}
      noResults={<Menu.Item disabled text={<i>No worlds</i>} />}
    >
      <Button minimal alignText={Alignment.LEFT} rightIcon={rightIcon}>
        <H3 style={{ margin: 0 }}>{world ? world.name : <i>Select world</i>}</H3>
      </Button>
    </Select>
  );
};
