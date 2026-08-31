import Header from './Header.tsx'
import Footer from './Footer.tsx'
import SearchBar from "./SearchBar.tsx";
import { BrowserRouter, Routes, Route } from "react-router-dom"

function App() {
  return(
      <BrowserRouter>
          <Header/>
          <Routes>
              <Route path="/" element={<SearchBar/>}/>
              <Route path="/song/:id" element={<Footer/>}/>
          </Routes>
          <Footer/>
      </BrowserRouter>
  )
}

export default App
