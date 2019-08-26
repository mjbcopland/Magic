type Maybe<T> = T | null;

declare module '*.gql' {
  import { DocumentNode } from 'graphql';
  const document: DocumentNode;

  export default document;
}
