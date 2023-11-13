import Cookies from 'js-cookie';

export const getUserData = () => {
  return {
    access: Cookies.get('access.myblog'),
    refresh: Cookies.get('refresh.myblog'),
    username: Cookies.get('username.myblog'),
    expiredTime: Cookies.get('expiredTime.myblog')
  };
};

export const isAuthenticated = () => {
  return Boolean(Cookies.get('access.myblog'));
};

export const clearUserData = () => {
  Cookies.remove('access.myblog');
  Cookies.remove('refresh.myblog');
  Cookies.remove('username.myblog');
  Cookies.remove('expiredTime.myblog');
};
