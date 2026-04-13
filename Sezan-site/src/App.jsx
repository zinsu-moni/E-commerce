import {Routes,Route} from "react-router-dom"
import Landing from "./Pages/Landing"
import ProductList from "./Pages/ProductList"
import ProductDetail from "./Pages/ProductDetail"
import CheckOut from "./Pages/CheckOut"
import Login from "./Pages/Login"
function App() {
  return (
    <>
    <Routes>
      <Route path="/" element={<Landing/>} />
      <Route path="/login" element={<Login />} />
      <Route path="/products" element={<ProductList />} />
      <Route path="/products/:id" element={<ProductDetail />} />
      <Route path="/checkout" element={<CheckOut />} />
    </Routes>
    </>
  )
}

export default App
