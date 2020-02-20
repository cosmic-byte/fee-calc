const path = require('path');
const fs = require('fs');
const webpack = require('webpack');
const dotenv = require('dotenv');

module.exports = (env) => {

    const currentPath = path.join(__dirname);
    const basePath = currentPath + '/.env';
    const envPath = basePath + '.' + env.ENVIRONMENT;
    const finalPath = fs.existsSync(envPath) ? envPath : basePath;

    const fileEnv = dotenv.config({ path: finalPath }).parsed;

    const envKeys = Object.keys(fileEnv).reduce((prev, next) => {
        prev[`process.env.${next}`] = JSON.stringify(fileEnv[next]);
        return prev;
    }, {});

    return {
        entry: [
    'babel-polyfill',
    './public/js/app.js',
    './public/css/spinner.css',
    './public/css/styles.css',
    './public/css/toaster.css',
  ],
        output: {
        path: __dirname,
        publicPath: '/',
        filename: 'bundle.js'
      },
        module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: [
          'babel-loader',
         ]
      },
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader',
        ]
      }
    ]
  },
        plugins: [
            new webpack.DefinePlugin(envKeys)
        ]
    }
};