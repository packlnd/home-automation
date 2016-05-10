//
//  FirstViewController.swift
//  home-automation-controller
//
//  Created by Patrik Ackland on 3/12/16.
//  Copyright © 2016 Patrik Ackland. All rights reserved.
//

import UIKit
import Alamofire

class LampViewController: UIViewController {
    let ip = "http://10.157.160.44:5000/"
    override func viewDidLoad() {
        super.viewDidLoad()
        let action = "status"
        let url = "\(ip)\(action)"
        let status = Alamofire.request(.GET, url)
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func onOffSwitch(sender: UISwitch) {
        let action = sender.on ? "on" : "off"
        let url = "\(ip)\(action)"
        Alamofire.request(.GET, url)
    }
}