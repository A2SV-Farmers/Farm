import { Link } from "react-router-dom";
import styles from "./Login.module.css";

const Login = () => {
  return (
    <div className={styles.logIn}>
      <form className={styles.loginChild}>
        <div className={styles.form}>
          <div className={styles.formItems}>
            <div className={styles.loginItem}>
              <label className={styles.label} for="username">
                User Name
              </label>
              <input autoComplete="off" name="username" id="username" />
            </div>

            <div className={styles.loginItem}>
              <label className={styles.label} for="password">
                Password
              </label>
              <input type="password" name="password" id="password" />
            </div>
          </div>
          <div className={styles.submit}>
            <button className={styles.button}>Log In</button>
          </div>
        </div>
        <p className={styles.footer}>
          Forgot password? <Link to="/signup">Reset here</Link>
        </p>
      </form>
    </div>
  );
};

export default Login;
