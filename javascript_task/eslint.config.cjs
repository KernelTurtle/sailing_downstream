module.exports = [
  {
    files: ["**/*.js"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      globals: {
        browser: true,
        node: true,
        jest: true,
      },
    },
    plugins: {
      jest: require("eslint-plugin-jest"),
      prettier: require("eslint-plugin-prettier"),
    },
    rules: {
      "no-console": "warn",
      "no-unused-vars": "warn",
      "prettier/prettier": [
        "error",
        {
          singleQuote: true,
          trailingComma: "es5",
        },
      ],
    },
  },
  {
    files: ["**/__tests__/**/*.js", "**/?(*.)+(spec|test).js"],
    plugins: {
      jest: require("eslint-plugin-jest"),
    },
    rules: {
      ...require("eslint-plugin-jest").configs.recommended.rules,
    },
  },
];
