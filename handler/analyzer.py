from tabulate import tabulate

def analyze_portfolio(portfolio: dict):
    
    total_portfolio = {"leveraged": 0, "unleveraged": 0}
    tabulate_lists = [["Asset Type".upper(), "Amount".upper()]]
    total_cash = 0

    def handle(asset_type: str):

        cash = 0
        tabulate_lists.append([asset_type.upper(), None]) # type: ignore
        
        key_list = list(portfolio[asset_type].keys())
        
        for key in key_list:
            item = portfolio[asset_type][key]
            if isinstance(item, list):
                total_portfolio[asset_type] += item[0]
                cash += item[1]
                tabulate_lists.append([
                    key.replace('_', ' ').strip().title(), 
                    item[0]]) # type: ignore
            elif isinstance(item, int):
                total_portfolio[asset_type] += item
                tabulate_lists.append([
                    key.replace('_', ' ').strip().title(),
                    item]) # type: ignore
            else:
                raise TypeError("Wrong input type")
        
        tabulate_lists.append(["TOTAL "+asset_type.upper()+" POSITION", total_portfolio[asset_type]]) # type: ignore
        tabulate_lists.append(["CASH IN "+asset_type.upper()+"\nACCOUNTS", cash]) # type: ignore
        tabulate_lists.append(['-----------------------------', '--------'])
        
        return cash

    total_cash += handle('unleveraged')
    total_cash += handle('leveraged')

    total_position_ = total_portfolio['leveraged'] + total_portfolio['unleveraged']
    leveraged_percentage = total_portfolio['leveraged'] / total_position_

    # tabulate_lists.append(['-----------------------------', '--------'])
    tabulate_lists.append(['TOTAL CASH', total_cash]) # type: ignore
    tabulate_lists.append(["TOTAL POSITION", total_position_]) # type: ignore
    tabulate_lists.append(["TOTAL PORTFOLIO".upper(), total_position_ + total_cash]) # type: ignore
    tabulate_lists.append(["Percentage Leveraged Assets".upper(), str(100*round(leveraged_percentage,3))+'%']) # type: ignore

    print(tabulate(
        tabulate_lists, 
        headers="firstrow", 
        tablefmt='pipe'))