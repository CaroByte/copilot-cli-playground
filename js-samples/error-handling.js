function parseConfig(jsonText) {
  try {
    const config = JSON.parse(jsonText);
    if (!config.environment) {
      throw new Error('Missing required "environment" setting.');
    }
    return config;
  } catch (error) {
    console.error('Could not parse configuration:', error.message);
    return { environment: 'development', retries: 1 };
  }
}

const config = parseConfig('{"retries": 3}');
console.log('Using config:', config);
