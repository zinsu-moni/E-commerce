import { Link } from "react-router-dom"
import Container from "../assets/Container.svg" 
import {FaShoppingCart, FaUserCircle,FaSearch } from "react-icons/fa"

function Navbar(){
    return(
        <nav className="flex flex-row items-center justify-between p-3 h-[80px] z-auto] border-b border-gray-200  bg-[#FFFFFF] shadow-xl" >
            <div className="pl-3">
                <Link><img src={Container} alt="" /></Link>
            </div>
            <div className="centre">
                <ul className="flex flex-row gap-6 text-[#64748B] font-medium text-lg">
                    <li><Link to="/products">Shop</Link></li>
                    <li><Link to="/products/:id">Collections</Link></li>
                    <li><Link to="/login">New Arrivals</Link></li> 
                </ul>
            </div>
            <div className="flex flex-row items-center gap-4  ">
              <div className="relative flex items-center">
                <FaSearch className="absolute left-3 text-gray-400 text-sm" />
                <input
                type="text"
                placeholder="Search curated goods..."
                className="pl-10 pr-3 h-[52px] w-[234.4px] bg-[#F2F3FF] rounded-full text-sm outline-none w-full"/>
             </div> 
               <section className="flex flex-row items-center gap-4 ">
                <Link to="/checkout"><FaShoppingCart className="text-[19px] text-[#5054FF]" /></Link>
                <Link to="/login"><FaUserCircle className="text-[19px] text-[#5054FF]" /></Link>
               </section>
            </div>
        </nav>
    )
}
export default Navbar
