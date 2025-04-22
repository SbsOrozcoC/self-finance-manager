import axios from 'axios'

const API_URL = 'http://localhost:8000'

export const login = async (username: string, password: string): Promise<string> => {
  const data = new URLSearchParams()
  data.append('username', username)
  data.append('password', password)

  const response = await axios.post<{ access_token: string }>(
    `${API_URL}/auth/login`,
    data, // ← envía como body, no como params
    {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    }
  )

  const token = response.data.access_token
  localStorage.setItem('token', token)

  return token
}

export const getToken = (): string | null => localStorage.getItem('token')

export const logout = (): void => {
  localStorage.removeItem('token')
}
