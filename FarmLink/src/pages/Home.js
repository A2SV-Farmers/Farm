import { NavLink } from "react-router-dom";
import styles from "./Home.module.css";
const Home = () => {
  return (
    <div className={styles.home}>
      <img
        className={styles.logoImg}
        alt=""
        src="/sustainable-farming-green-leaf-wood-brown-sleek-logo-1-1@2x.png"
      />
      <NavLink to="login">
        <button className={styles.btn}>Get Started</button>
      </NavLink>
    </div>
  );
};

export default Home;
