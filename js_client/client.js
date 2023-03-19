const loginForm = document.getElementById('login-form')
const baseEndpoint = "http://localhost:7890/api"
if (loginForm) {
  loginForm.addEventListener('submit', handleLogin)
}

const handleLogin = async (event) => {
  console.log(`🧳%cclient.js:9 - event`, 'font-weight:bold; background:#2fd000;color:#fff;'); //DELETEME
  console.log(event); // DELETEME
  event.preventDefault()
  const loginEndpoint = `${baseEndpoint}/token/`
  let loginFormData = new FormData(loginForm)
  let loginObjectData = Object.fromEntries(loginFormData)
  let bodyStr = JSON.stringify(loginObjectData)

  const options = {
    method: "POST",
    headers: {
      "ContentType": "application/json"
    },
    body: bodyStr
  }

  try {
    const response = await fetch(loginEndpoint, options);
    const x = await response.json()
    console.log(`🎇%cclient.js:30 - x`, 'font-weight:bold; background:#738c00;color:#fff;'); //DELETEME
    console.log(x); // DELETEME
  } catch (err) {
    console.log('err', err)
  }
}
