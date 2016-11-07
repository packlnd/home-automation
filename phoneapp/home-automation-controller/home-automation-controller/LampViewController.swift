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
    @IBOutlet weak var onOffSwitch: UISwitch!
    let ip = "http://10.157.160.44:5000/"
    
    override func viewDidAppear(animated: Bool) {
        super.viewDidAppear(animated)
        let action = "lamp_status"
        let url = "\(ip)\(action)"
        Alamofire.request(.GET, url)
            .validate()
            .responseJSON { response in
                if let JSON = response.result.value {
                    if let status = JSON["status"] as? Int {
                        if status == 0 {
                            self.onOffSwitch.setOn(false, animated: false)
                        }
                    }
                }
        }
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