import {Routes,Route} from "react-router-dom"
import Landing from "./Pages/Landing"
import ProductList from "./Pages/ProductList"
import ProductDetail from "./Pages/ProductDetail"
import CheckOut from "./Pages/CheckOut"
import Signup from "./Pages/Signup"
import Login from "./Pages/Login"
import Dashboard from "./Pages/Dashboard"
function App() {
  return (
    <>
     <Routes>
       <Route path="/" element={<Landing/>} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
       <Route path="/products" element={<ProductList />} />
       <Route path="/products/:id" element={<ProductDetail />} />
        <Route path="/checkout" element={<CheckOut />} />
        <Route path="/dashboard" element={<Dashboard />} />
     </Routes>
    </>
  )
}

export default App
