import { Link } from "react-router-dom"
import { HiOutlineShoppingBag, HiOutlineUser } from "react-icons/hi2";
import { HiShoppingBag, HiUser } from "react-icons/hi";
const Navbar = () => {
    return (
      <div className="w-[100%] h-[80px] bg-[#FFFFFF] flex items-center justify-between px-[20px]">
        <h1 className="w-[172px] h-[28px] font-black text-[20px] leading-[28px] tracking-[-1px]">
          The Fluid Architect
        </h1>
        {/* centre */}
        <ul className="flex flex-row gap-[32px]">
          <li>
            <Link>Shop All</Link>
          </li>
          <li>
            <Link>Collections</Link>
          </li>
          <li>
            <Link>Sustainability</Link>
          </li>
          <li>
            <Link>Journals</Link>
          </li>
        </ul>
        <div className="flex flex-row w-[79.9px] h-[36px] gap-[15.99px] items-center 0">
          <Link>
            <HiOutlineShoppingBag className="w-[20px] h-[24px] hover:bg-[#3132ED] transition-colors duration-200" />
          </Link>
          <Link>
            <HiOutlineUser className="w-[20px] h-[20px] hover:bg-[#3132ED] transition-colors duration-200" />
          </Link>
        </div>
      </div>
    );
}
export default Navbar;