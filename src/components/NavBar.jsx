import { NavLink } from 'react-router-dom';

function NavBar() {
  return (
    <nav>
      <NavLink to="/" end>Inicio</NavLink>
      <NavLink to="/minijuego1">Minijuego 1</NavLink>
      <NavLink to="/minijuego2">Minijuego 2</NavLink>
      <NavLink to="/minijuego3">Minijuego 3</NavLink>
      <NavLink to="/minijuego4">Minijuego 4</NavLink>
      <NavLink to="/minijuego5">Minijuego 5</NavLink>
    </nav>
  );
}

export default NavBar;