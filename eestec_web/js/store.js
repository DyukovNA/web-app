function getAccessToken() {
  return localStorage.getItem("access-token");
}

function storeAccessToken(token) {
  localStorage.setItem("access-token", token);
}
