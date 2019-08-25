import '@babel/polyfill';
import 'normalize.css';

// override the webpack loader with global CSS for Blueprint
import '!css-loader?modules=global!@blueprintjs/core/lib/css/blueprint.css';

// react-hot-loader has side effects and needs to be imported before React and related modules
import 'react-hot-loader';

import React from 'react';
import ReactDOM from 'react-dom';

import { FocusStyleManager } from '@blueprintjs/core';

import { App } from './app';

import '~/index.scss';

FocusStyleManager.onlyShowFocusOnTabs();

ReactDOM.render(<App />, document.getElementById('root'));
