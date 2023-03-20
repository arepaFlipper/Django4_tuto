const contentContainer = document.getElementById('content-container');
const loginForm = document.getElementById('login-form');
const searchForm = document.getElementById('search-form');
const baseEndpoint = "http://localhost:7890/api/auth/";

if (loginForm) {
  loginForm.addEventListener('submit', handleLogin);
}

if (searchForm) {
  loginForm.addEventListener('submit', handleSearch);
}

const handleLogin = async (event) => {
  event.preventDefault();
  const loginEndpoint = `${baseEndpoint}/token/`;
  let loginFormData = new FormData(loginForm);
  let loginObjectData = Object.fromEntries(loginFormData);
  let bodyStr = JSON.stringify(loginObjectData);

  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: bodyStr,
  };

  try {
    const response = await fetch(loginEndpoint, options);
    const data = await response.json();
    handleAuthData(data, getProductList);
  } catch (err) {
    console.log('err', err);
  }
}

const handleSearch = (event) => {
  event.preventDefault()
  let formData = new FormData(searchForm)
  let data = Object.fromEntries(formData)
  let searchParams = new URLSearchParams(data)
  const endpoint = `${baseEndpoint}/search/?${searchParams}`
  const headers = {
    "Content-Type": "application/json",
  }
  const authToken = localStorage.getItem('access')
  if (authToken) {
    headers['Authorization'] = `Bearer ${authToken}`
  }
  const options = {
    method: "GET",
    headers: headers
  }
  fetch(endpoint, options) //  Promise
    .then(response => {
      return response.json()
    })
    .then(data => {
      const validData = isTokenNotValid(data)
      if (validData && contentContainer) {
        contentContainer.innerHTML = ""
        if (data && data.hits) {
          let htmlStr = ""
          for (let result of data.hits) {
            htmlStr += "<li>" + result.title + "</li>"
          }
          contentContainer.innerHTML = htmlStr
          if (data.hits.length === 0) {
            contentContainer.innerHTML = "<p>No results found</p>"
          }
        } else {
          contentContainer.innerHTML = "<p>No results found</p>"
        }
      }
    })
    .catch(err => {
      console.log('err', err)
    })
}

const handleAuthData = (authData, callback) => {
  localStorage.setItem('access', authData.access);
  localStorage.setItem('refresh', authData.refresh);
  if (callback) {
    callback();
  }
}

const writeToContainer = (data) => {
  if (contentContainer) {
    contentContainer.innerHTML = "<pre>" + JSON.stringify(data) + "</pre>";
  }
}

const isTokenNotValid = (jsonData) => {
  if (jsonData?.code === "token_not_valid") {
    alert("Please login again");
    return false;
  }
  return true;

}

const validateJWTToken = async () => {
  const endpoint = `${baseEndpoint}/token/verify/`
  const body = JSON.stringify({
    token: localStorage.getItem('access'),
  })
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body,
  };
  try {
    const res = fetch(endpoint, options);
    const dat0 = await res.json()
    isTokenNotValid(dat0);

  } catch (error) {

  }
}

const getProductList = async () => {
  const endpoint = `${baseEndpoint}/products/`;
  const options = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${localStorage.getItem('access')}`,
    }
  };
  const response = await fetch(endpoint, options);
  const data = await response.json();
  isTokenNotValid(data);
  if (validData) {
    writeToContainer(data)
  }
};

const getFetchOptions = (method = "GET", body) => {
  const options = {
    method,
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${localStorage.getItem('access')}`,
    },
    body,
  }
  return options;
}

validateJWTToken();
