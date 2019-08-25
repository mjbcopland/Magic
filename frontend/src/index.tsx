import '@babel/polyfill';
import 'normalize.css';

import '!css-loader?modules=global!@blueprintjs/core/lib/css/blueprint.css';

import 'react-hot-loader';

import React from 'react';
import ReactDOM from 'react-dom';

import { FocusStyleManager } from '@blueprintjs/core';

import { App } from './app';

FocusStyleManager.onlyShowFocusOnTabs();

ReactDOM.render(<App />, document.getElementById('root'));
