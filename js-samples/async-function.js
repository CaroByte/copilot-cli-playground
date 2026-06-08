async function fetchUserProfile(userId) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ id: userId, name: 'Caro', role: 'maintainer' });
    }, 300);
  });
}

async function showUserProfile() {
  const profile = await fetchUserProfile(101);
  console.log(`Loaded ${profile.name} (${profile.role})`);
}

showUserProfile().catch((error) => {
  console.error('Unexpected async error:', error.message);
});
