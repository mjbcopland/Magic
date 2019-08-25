const path = require('path');
const webpack = require('webpack');
const merge = require('webpack-merge');

const HtmlWebPackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');

const package = require('./package.json');

const config = {
  common: {
    resolve: {
      alias: {
        '~': path.resolve(__dirname, 'src/'),
        'react-dom': '@hot-loader/react-dom',
      },
      extensions: ['.ts', '.tsx', '.js', '.jsx'],
    },
    module: {
      rules: [
        {
          include: /\.html$/,
          use: ['html-loader'],
        },
        {
          include: /\.mp3$/,
          use: [
            {
              loader: 'file-loader',
              options: {
                name: '[path][name].[ext]',
                publicPath: '/',
              },
            },
          ],
        },
        {
          include: /\.(sa|sc|c)ss$/,
          use: [{ loader: 'css-loader', options: { modules: true } }, 'sass-loader'],
        },
        {
          include: /\.(j|t)sx?$/,
          exclude: /node_modules/,
          use: ['babel-loader', 'ts-loader'],
        },
      ],
    },
    plugins: [new HtmlWebPackPlugin({ hash: true, title: package.name, template: 'src/index.ejs' })],
    optimization: {
      minimizer: [new TerserPlugin({ parallel: true, sourceMap: true }), new OptimizeCSSAssetsPlugin()],
    },
    devServer: {
      historyApiFallback: true,
      host: '0.0.0.0',
      public: 'localhost',
    },
  },
  development: {
    mode: 'development',
    devtool: 'inline-source-map',
    module: {
      rules: [
        {
          include: /\.(sa|sc|c)ss$/,
          use: ['style-loader'],
          enforce: 'post',
        },
      ],
    },
    plugins: [new webpack.EnvironmentPlugin({ NODE_ENV: 'development' })],
  },
  production: {
    mode: 'production',
    devtool: 'source-map',
    module: {
      rules: [
        {
          include: /\.(sa|sc|c)ss$/,
          use: [MiniCssExtractPlugin.loader],
          sideEffects: true,
          enforce: 'post',
        },
      ],
    },
    plugins: [new webpack.EnvironmentPlugin({ NODE_ENV: 'production' }), new MiniCssExtractPlugin()],
  },
};

module.exports = (env) => merge.smart(config[env], config.common);
