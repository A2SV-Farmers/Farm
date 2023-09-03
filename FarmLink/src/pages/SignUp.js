import { Link } from "react-router-dom";
import styles from "./SignUp.module.css";
const SignUp = () => {
  return (
    <div className={styles.signUp}>
      <form className={styles.signUpChild}>
        <div className={styles.form}>
          <div className={styles.formItems}>
            <div className={styles.signUpItem}>
              <label className={styles.label} for="username">
                User Name
              </label>
              <input autoComplete="off" name="username" id="username" />
            </div>
            <div className={styles.signUpItem}>
              <label className={styles.label} for="phone">
                Phone
              </label>
              <input name="phone" id="phone" />
            </div>
            <div className={styles.signUpItem}>
              <label className={styles.label} for="region">
                Region
              </label>
              <input name="region" id="region" />
            </div>
            <div className={styles.signUpItem}>
              <label className={styles.label} for="password">
                Password
              </label>
              <input type="password" name="password" id="password" />
            </div>
            <div className={styles.signUpItem}>
              <label className={styles.label} for="conf-password">
                Password
              </label>
              <input type="password" name="password" id="conf-password" />
            </div>
          </div>
          <div className={styles.submit}>
            <button className={styles.button}>Sign Up</button>
          </div>
        </div>
        <p className={styles.footer}>
          Already have an account? <Link to="/login">Login</Link>
        </p>
      </form>
    </div>
  );
};

export default SignUp;
